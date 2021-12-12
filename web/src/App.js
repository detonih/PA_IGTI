/* eslint-disable import/no-anonymous-default-export */
import React from 'react';
import useForm from './hooks/useForm';
import api from './services/api'

export default () => {
  const [{ values, loading }, handleChange, handleSubmit] = useForm();

  const getInfo = async () => {
    console.log(`http://0.0.0.0:8000/info/${values}`);
    
    try {
      const response = await api.get(`http://0.0.0.0:8000/info/${values}`);
      console.log(response);
    } catch (error) {
      console.error(error);
    }
    
  };

  return (
    <div>
      <h1>Market</h1>
      <form onSubmit={handleSubmit(getInfo)}>
        <label>
          Choose your company:
          <select onChange={handleChange}>
            <option value="GOOGL">GOOGL</option>
            <option value="MSFT">MSFT</option>
          </select>
        </label>
        {/* <input type="submit" value="Enviar" /> */}
        <button type="submit">{loading ? 'Enviando...' : 'Enviar'}</button>
      </form>
    </div>
  );
};