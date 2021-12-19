/* eslint-disable import/no-anonymous-default-export */
import React from 'react';
import useForm from './hooks/useForm';
import api from './services/api'
import './App.css'

export default () => {
  const [{ values, loading }, handleChange, handleSubmit] = useForm();

  const getInfo = async () => {
    try {
      const response = await api.get(`http://0.0.0.0:8000/info/${values[Object.keys(values)[0]]}`);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  const startConsumer = async () => {
    try {
      const response = await api.get(`http://0.0.0.0:8000/start_consumer`);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className='form-box'>
      <h1>Market</h1>
      <form onSubmit={handleSubmit(getInfo)}>
        <label>
          Choose your company ticker:
          <select className="custom-select" onChange={handleChange}>
            <option value="GOOGL" name="GOOGL">GOOGL (Google)</option>
            <option value="MSFT" name="MSFT">MSFT (Microsoft)</option>
            <option value="AMZN" name="AMZN">AMZN (Amazon)</option>
          </select>
        </label>
        {/* <input type="submit" value="Enviar" /> */}
        <div>
        <button className='submitBut' type="submit">{loading ? 'Enviando...' : 'Submit'}</button>
        </div>
      </form>
      <div>
        <label>
          Start Kafka consumer: 
        </label>
        <div>
        <button className='submitBut' onClick={handleSubmit(startConsumer)} type="button">Start consumer</button>
        </div>
      </div>
    </div>
  );
};