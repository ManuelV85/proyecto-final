import React from "react";
import { useForm } from "react-hook-form";

export const Emailpassword = () => {
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
        <label for="exampleInputEmail1" className="form-label">
          Ingrese su email
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
      </div>

      <div class="mb-3 ">
        <button type="submit" value="submit" className="btn btn-dark">
          Enviar E-mail
        </button>
      </div>
    </form>
  );
};
