import React from "react";

function Tarea({ id, texto, eliminartarea }) {
  return (
    <div className="contenedor-tarea">
      <div className="tarea-texto">
        <h2>{texto}</h2>
      </div>
      <div className="icono-eliminar" onClick={() => eliminartarea(id)}>
        x
      </div>
    </div>
  );
}

export default Tarea;
