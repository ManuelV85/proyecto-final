import { useNavigate } from "react-router-dom";
import React from "react";
import { Logo } from "../component/Logo";
import {useJwt} from "react-jwt"

export const Biker = () => {
  const userToken = localStorage.getItem("iProBike-token")
  const {token, isExpired} = useJwt(userToken)
  const navigate = useNavigate();
  const typeB = localStorage.getItem("iProBike-type")
  if (isExpired){
    navigate("/login")
  } else if (!isExpired && typeB == "ws"){
    navigate("/login")
  }

  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <Logo />
      </div>

      <button
        onClick={() => navigate("/userstore")}
        type="submit"
        className="btn btn-dark"
      >
        Visitar Tienda
      </button>
      <div className="mb-3">
        <button
          onClick={() => alert("proximamente")}
          type="submit"
          className="btn btn-dark"
        >
          Viajes
        </button>

        <button
          onClick={() => navigate("/sos")}
          type="submit"
          className="btn btn-danger"
        >
          S.O.S
        </button>
      </div>
    </form>
  );
};
