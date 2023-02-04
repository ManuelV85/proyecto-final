import { useState,useRef} from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import React from "react";
import { sendEmail } from "../service/emailService";


export const Registration = () => {
  const navigate = useNavigate();
  const url = process.env.BACKEND_URL

  const [email, setEmail] = useState("");
  const [user, setUser] = useState({
    email: "mail@mail.com",
    name: "Jhon Doe",
  });

  const [link, setLink] = useState("www.google.com");

  const verify = (_) => {
    if (email.localeCompare(user.email) != 0) throw Error("Invalid Email");
    let params = {
      to_email: user.email,
      to_name: user.name,
      to_link: link,
    };
    sendEmail(params);
  };

  

  const [isBike, setIsBike] = useState(true);
  const {
    register,
    handleSubmit,
    watch,
    getValues,
    formState: { errors },
  } = useForm();

  const onSubmit = async (dataUser) => {
   
    const route = isBike ? "users" : "ws";
    const response = await fetch(   
      `${url}/api/signin/${route}`,
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
    if (response["code"] == 1) {
      alert(response["response"]);
    } else if (response["code"] == 0) {
    
      
      sendEmail({to_email:dataUser.email,to_name:dataUser.first_name})
      navigate("/login",{state:{response:response["response"]}})
    };
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="contenedor-login">
      <div className="mb-3">
        <button
          onClick={() => setIsBike(false)}
          type="button"
          className="btn btn-dark"
        >
          Tienda
        </button>
        <button
          onClick={() => setIsBike(true)}
          type="button"
          className="btn btn-dark"
        >
          Ciclista
        </button>
      </div>
      <div className="mb-3">
        <label for="InputName" className="form-label">
          Nombre
        </label>
        <input
          type="text"
          className="form-control"
          id="InputName"
          {...register("first_name")}
        />
        {isBike ? (
          <>
            <label for="InputLastName" className="form-label">
              Apellido
            </label>
            <input
              type="text"
              className="form-control"
              id="InputLastName"
              {...register("last_name")}
            />
          </>
        ) : (
          <></>
        )}
        <label for="exampleInputEmail" className="form-label">
          E-mail
        </label>
        <input
         title="email"
         type="email"
        
         
          
          className="form-control"
          id="exampleInputEmail"
          {...register("email")}
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
        <label for="InputPassword" className="form-label">
          Contraseña
        </label>
        <input
          type="password"
          className="form-control"
          id="InputPassword"
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

        <label for="InputRepeatPassword" className="form-label">
          Repita contraseña
        </label>
        <input
          type="password"
          className="form-control"
          id="InputRepeatPassword"
          {...register("password2", {
            required: {
              value: true,
              message: "Necesitas este campo",
            },
          })}
        />
        {watch("password") !== watch("password2") && getValues("password2") ? (
          <h1 style={{ color: "red", fontSize: "16px" }}>
            Contraseñas no coinciden
          </h1>
        ) : null}

        <label for="InputAddress" className="form-label">
          Direccion
        </label>
        <input
          type="text"
          className="form-control"
          id="InputAddress"
          {...register("address")}
        />

        {!isBike ? (
          <>
            <label for="InputHours" className="form-label">
              horario Ej:(8:00 a 17:00)
            </label>
            <input
              type="text"
              className="form-control"
              id="InputHours"
              {...register("hours")}
            />
            <label for="InputScheduling" className="form-label">
              dias Ej:(Lun-Mar)
            </label>
            <input
              type="text"
              className="form-control"
              id="InputScheduling"
              {...register("scheduling")}
            />
          </>
        ) : (
          <></>
        )}
      </div>
      <button type="submit" className="btn btn-dark" >
        Crear cuenta
      </button>
    </form>
  );
};
