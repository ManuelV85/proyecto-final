import React from "react";

export const Recuperate = () => {
  return (
    <form className="contenedor-login">
      <div class="mb-3">
        <label for="exampleInputPassword1" className="form-label">
          Contraseña
        </label>
        <input
          type="password"
          className="form-control"
          id="exampleInputPassword1"
        />

        <label for="exampleInputPassword1" className="form-label">
          Repetir contraseña
        </label>
        <input
          type="password"
          className="form-control"
          id="exampleInputPassword1"
        />
        <br></br>

        <button
          onClick={() => navigate("/login")}
          type="submit"
          className="btn btn-dark"
        >
          Recuperar
        </button>
      </div>
    </form>
  );
};
