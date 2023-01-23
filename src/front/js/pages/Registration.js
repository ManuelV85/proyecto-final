import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import React, { useState } from "react";

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
        <label for="name" className="form-label">
          Name
        </label>
        <input
          type="Name"
          className="form-control"
          id="Name"
          aria-describedby="name"
        />

        <label for="last-name" className="form-label">
          Last-Name
        </label>
        <input
          type="last-name"
          className="form-control"
          id="Last-name"
          aria-describedby="last-name"
        />

        <label for="exampleInputEmail1" className="form-label">
          E-mail{" "}
        </label>
        <input
          title="email"
          name="user_email"
          type="email"
          className="form-control"
          id="email"
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
        <label for="password" className="form-label">
          Pasword
        </label>
        <input
          title="Password"
          type="password"
          className="form-control"
          id="password"
          aria-describedby="password"
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

        <label for="repeat-password" className="form-label">
          Repeat Password
        </label>
        <input
          type="password"
          className="form-control"
          id="password"
          aria-describedby="password"
        />

        <label for="address" className="form-label">
          Addressn
        </label>
        <input
          type="address"
          className="form-control"
          id="addrress"
          aria-describedby="addrress"
        />

        {mostrarComponente ? (
          <>
            <label for="horario" className="form-label">
              horario
            </label>
            <input
              type="Horario"
              className="form-control"
              id="horario"
              aria-describedby="horario"
            />
          </>
        ) : (
          <></>
        )}
      </div>
      <button type="submit" className="btn btn-dark" value="Send">
        Create Acount
      </button>
    </form>
  );
};
