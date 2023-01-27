import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { useNavigate } from "react-router-dom";
import { Logo } from "../component/Logo";

export const Horario = () => {
  const navigate = useNavigate();

  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <Logo />
      </div>
      <div class="mb-3 row">
        <div className="contenidohorario">
          <h1 >Horario</h1>
          <p className="info">Lunes a viernes</p>
          <p>9:00 - 19:00</p>
          <p>Manuel rodriguez,vitacura</p>
        </div>
      </div>
    </form>
  );
};
