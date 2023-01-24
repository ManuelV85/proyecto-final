import { useNavigate } from "react-router-dom";
import React from "react";
import { Logo } from "../component/Logo";



export const Sos = () => {
  const navigate = useNavigate();
  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <Logo />
        
      </div>
     

    
    </form>
  );
};
