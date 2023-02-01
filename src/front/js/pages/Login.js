import { useNavigate } from "react-router-dom";
import { Logo } from "../component/Logo";
import  React, {useContext, useState} from 'react'
import { useForm } from "react-hook-form";
import {Context} from '../store/appContext'


export const Login = () => {
  const navigate = useNavigate();
  const [mostrarComponente, setMostrarComponente] = useState(false);
  const [mostrarrComponente, setMostrarrComponente] = useState(true);
  const [recuperate, setRecuperateComponente] = useState(false);
  const {store} = useContext(Context)

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (dataUser) => {
    const response = await fetch(
      "https://3001-manuelv85-proyectofinal-mqix53vw88a.ws-us84.gitpod.io/api/login",
      {
        crossDomain: true,
        method: "POST",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        referrerPolicy: "no-referrer",
        body: JSON.stringify(dataUser),
      }
    ).then((response) => response.json());

    if (response["code"] >= 2) {
      alert(response["response"]);
    } else {
      store.user = {type:response["type"], id: response["id"], token: response["token"]}
      localStorage.setItem("iProBike-token", store.user.token)
      console.log(store.user) //<-- comprobar datos
      const isBike = response["type"] == "user" ? true : false;
      if (isBike) {
        navigate("/biker");
      } else {
        navigate("/menustore");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="contenedor-login">
      <div className="mb-3">
        <Logo />
      </div>
      <div className="mb-3">
        <label for="InputEmail" className="form-label">
          E-mail{" "}
        </label>
        <input
          name="email"
          type="text"
          className="form-control"
          id="InputEmail"
          aria-describedby="emailHelp"
          placeholder="ingrese Email"
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
        <di className="error">
          {errors.email && <span>{errors.email.message}</span>}
        </di>
      </div>
      <div class="mb-3">
        <label for="InputPassword" className="form-label">
          Contraseña
        </label>
        <input
          type="password"
          name="password"
          className="form-control"
          id="InputPassword"
          placeholder="ingrese contraseña"
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
      </div>

      <div class="mb-3 ">
        <button type="submit" value="submit" className="btn btn-dark">
          Entrar
        </button>

        <button
          onClick={() => navigate("/Emailpassword")}
          type="submit"
          className="btn btn-dark"
        >
          Recuperar contraseña
        </button>
      </div>
    </form>
  );
};
