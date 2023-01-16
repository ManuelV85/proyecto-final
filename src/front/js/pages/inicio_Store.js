import { useNavigate } from "react-router-dom";

import React from "react";

export const MenuStore = () => {
  const navigate = useNavigate();

  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <img
          src="https://cdn.pixabay.com/photo/2012/02/16/12/27/bicycle-13501_960_720.jpg"
          width="300px"
          ALIGN="center"
        ></img>

        <button
          onClick={() => navigate("/upload_item")}
          type="submit"
          className="btn btn-dark"
        >
          Cargar Producto
        </button>

        <button
          onClick={() => navigate("/tableinventary")}
          type="submit"
          className="btn btn-dark"
        >
          Inventario
        </button>

        <button
          onClick={() => navigate("/")}
          type="submit"
          className="btn btn-dark"
        >
          {" "}
          Direccion/horario de atencion
        </button>
      </div>
    </form>
  );
};
