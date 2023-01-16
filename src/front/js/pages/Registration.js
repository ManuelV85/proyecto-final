import { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import React from "react";

export const Registration = () => {
  const navigate = useNavigate();

  const [mostrarComponente, setMostrarComponente] = useState(true);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (evento) => {
    console.log(evento);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="contenedor-login">
      <div className="mb-3">
        <button
          onClick={() => setMostrarComponente(true)}
          type="button"
          className="btn btn-dark"
        >
          workshop
        </button>
        <button
          onClick={() => setMostrarComponente(false)}
          type="button"
          className="btn btn-dark"
        >
          biker
        </button>
      </div>
      <div className="mb-3">
        <label for="exampleInputEmail1" className="form-label">
          Name
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
        />

        <label for="exampleInputEmail1" className="form-label">
          Last-Name
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
        />

        <label for="exampleInputEmail1" className="form-label">
          E-mail{" "}
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          {...register("email", {
            required: {
              value: true,
              message: "Necesitas este campo",
            },
            pattern: {
              value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
              message: "El formato no es correcto",
            },
          })}
        />
        <div className="error">
          {errors.email && <span>{errors.email.message}</span>}
        </div>
        <label for="exampleInputEmail1" className="form-label">
          Pasword
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          {...register("password", {
            required: {
              value: true,
              message: "Necesitas este campo",
            },
            minLength: {
              value: 6,
              message: "la contrasena debe tener al menos 6 caracteres",
            },
          })}
        />
         <div className="error">
          {errors.password && <span>{errors.password.message}</span>}
        </div>

        <label for="exampleInputEmail1" className="form-label">
          Repeat Password
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
        />

        <label for="exampleInputEmail1" className="form-label">
          Addressn
        </label>
        <input
          type="email"
          className="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
        />

        {mostrarComponente ? (
          <>
            <label for="exampleInputEmail1" className="form-label">
              horario
            </label>
            <input
              type="email"
              className="form-control"
              id="exampleInputEmail1elim"
              aria-describedby="emailHelp"
            />
          </>
        ) : (
          <></>
        )}
      </div>
      <button
       
        type="submit"
        className="btn btn-dark"
      >
        Create Acount
      </button>
    </form>
  );
};
