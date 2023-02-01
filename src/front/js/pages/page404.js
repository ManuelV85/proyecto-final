import { useNavigate } from "react-router-dom";
import React from "react";
import { Logo } from "../component/Logo";



export const Page404 = () => {
  const navigate = useNavigate();

  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <Logo />
      </div>
      <div className="mb-3">
        <div className="DATO">
          <h1>PAGINA NO ENCONTRADA 404</h1>
                 </div>
      </div>
      <button
        onClick={() => navigate("/login")}

type="submit"
        className="btn btn-dark"
      >
        Regresar
      </button>
      
    </form>
  );
};
