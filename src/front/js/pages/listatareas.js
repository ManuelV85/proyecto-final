import React, { useState } from "react";
import Tarea from "./tarea";
import { TareasFormulario } from "./tareaFormulario";

export const Listadetareas = () => {
  const [tareas, setTareas] = useState([]);

  const agregartarea = (tarea) => {
    const tareaactualizada = [tarea, ...tareas];
    setTareas(tareaactualizada);
  };

  const eliminartarea = (id) => {
    const tareaactualizada = tareas.filter((tarea) => tarea.id !== id);
    setTareas(tareaactualizada);
  };
  return (
    <>
      <TareasFormulario onSubmit={agregartarea} />
      <div className="tareas-lista-contenedor">
        {tareas.map((tarea) => (
          <Tarea
            key={tarea.id}
            id={tarea.id}
            texto={tarea.texto}
            eliminartarea={eliminartarea}
          />
        ))}
      </div>
    </>
  );
};
