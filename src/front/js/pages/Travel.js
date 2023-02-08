import React from "react";
import { Logo } from "../component/Logo";
import ruta1 from "./ImagenesViaje/ruta1.jpg";
import ruta2 from "./ImagenesViaje/ruta2.jpg";
import ruta3 from "./ImagenesViaje/ruta3.jpg";
import ruta5 from "./ImagenesViaje/ruta5.jpg";

export const Travel = () => {
  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <Logo />
      </div>
      <div className="mb-3">
        <div className="DATO">
          <h1 className="viajes">VIAJES</h1>
          <p className="listadoeventos">Listado de eventos disponibles</p>
        </div>
        <div
          id="carouselExampleControlsNoTouching"
          class="carousel slide"
          data-bs-touch="false"
        >
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div className="card-producto">
                <img src={ruta1} className="card-img-top" alt="..."></img>
                <input
                  className="form-controle"
                  value="Ruta: San Fernando - Rancagua"
                />

                <input
                  className="form-controle"
                  name="user_precio1"
                  value="Kilometros: 61.2"
                />
                <input
                  className="form-controle"
                  name="user_precio2"
                  value="Hora estimada vuelta: 3hrs-7min "
                />
                <input
                  className="form-controle"
                  name="user_precio1"
                  value="Fecha:24-03-2023"
                />
              </div>
            </div>
            <div class="carousel-item">
              <div className="card-producto">
                <img src={ruta2} className="card-img-top" alt="..."></img>
                <input
                  className="form-controle"
                  name="user_producto2"
                  value="Ruta unidos por chile : curico - molina"
                />

                <input
                  className="form-controle"
                  name="user_precio2"
                  value="Kilometros :53.3"
                />
                <input
                  className="form-controle"
                  name="user_precio2"
                  value="Hora estimada vuelta: 2hrs-37min "
                />
                <input
                  className="form-controle"
                  name="user_precio2"
                  value="Fecha:27-04-2023"
                />
              </div>
            </div>

            <div class="carousel-item">
              <div className="card-producto">
                <img src={ruta3} className="card-img-top" alt="..."></img>
                <input
                  className="form-controle"
                  name="user_producto3"
                  value="Ruta nuestro sur  : Chillan - Parral"
                />

                <input
                  className="form-controle"
                  name="user_precio3"
                  value="Kilometros :100"
                />
                <input
                  className="form-controle"
                  name="user_precio3"
                  value="Hora estimada vuelta: 5hrs-13min "
                />
                <input
                  className="form-controle"
                  name="user_precio3"
                  value="Fecha 12-05-2023"
                />
              </div>
            </div>
            <div class="carousel-item">
              <div className="card-producto">
                <img src={ruta5} className="card-img-top" alt="..."></img>
                <input
                  className="form-controle"
                  type="producto"
                  name="user_producto4"
                  value="Ruta Temuco  : Temuco-Termas tolhuaca"
                />

                <input
                  className="form-controle"
                  
                  name="user_precio4"
                  value="Kilometros :116"
                />
              
              <input
                className="form-controle"
                
                name="user_precio4"
                value="Hora estimada vuelta: 6hrs-39min "
              />
              <input
                className="form-controle"
                
                name="user_precio4"
                value="Fecha 17-08-2023"
              />
              </div>
            </div>
          </div>
          <button
            class="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExampleControlsNoTouching"
            data-bs-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button
            class="carousel-control-next"
            type="button"
            data-bs-target="#carouselExampleControlsNoTouching"
            data-bs-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </form>
  );
};