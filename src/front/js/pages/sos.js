import { useNavigate } from "react-router-dom";
import React from "react";
import { Logo } from "../component/Logo";
import {Mapas} from "../pages/mapas";



export const Sos = () => {
  const navigate = useNavigate();
  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <Logo />
        <Mapas/>
      </div>
     

    
    </form>
  );
};
