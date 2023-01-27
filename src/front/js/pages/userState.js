import { useNavigate } from "react-router-dom";
import { Logo } from "../component/Logo";
import React, { useState } from "react";

const Categorias=[
  {
    "nombre" :"Todos los productos",
    "articulos" :["frenos","manubrio","parches","cadenas","neumaticos","sillin","casco","puño","punteras"],
  },
  {
    "nombre" :"repuestos",
    "articulos" :["frenos","manubrio","parches","cadenas","neumaticos"],
  },
  {
    "nombre" : "accesorios",
    "articulos" : ["sillin","casco","puño","punteras"],
    
  },
  {
    "nombre" : "suplementos",
    "articulos" : ["creatina","proteinas","aminoacidos","barras energeticas"],
    
  },
]


export const UserStore = () => {
  const navigate = useNavigate();

  const[idArticulos,setIdArticulos]=useState(-1);
 
 const handlerCargarArticulos=function(e){
  const opcion = e.target.value;
  console.log(opcion);

  setIdArticulos(opcion);

 }


  return (
    <form className="contenedor-login">
      <div className="mb-3">
        <div className="nombre-tienda">
          <Logo />
        </div>
        <div className="carrito">
          <button
            onClick={() => alert("proximamente")}
            type="submit"
            className="btn btn-dark"
          >
            <i className="fa-solid fa-cart-shopping"></i>{" "}
          </button>
        </div>

        <select name= "categorias" id="selCategoria" onClick={handlerCargarArticulos} className="form-select" aria-label="Default select example">
          <option value={-1} selected>Categoria</option>
         {
          Categorias.map((item,i)=>(
            <option key={"categoria" + i} value={i}>{item.nombre}</option>
          ))
         }
        </select>

        <select name ="articulos" id="selarticulos" className="form-select" aria-label="Default select example">
          <option value ={-1} selected>Productos</option>
          {
            idArticulos> -1 &&
            (
              Categorias[idArticulos].articulos.map((item,i)=>(
                <option key={"articulo"+i} value="">{item}</option>
              ))
            )
          }
        </select>

        
        <div
          id="carouselExampleControlsNoTouching"
          class="carousel slide"
          data-bs-touch="false"
        >
          <div class="carousel-inner">
            <div class="carousel-item active">
              <div  className="card-producto">
                 <img
                  src="https://cdn.pixabay.com/photo/2016/11/19/12/24/bicycle-1839005_960_720.jpg"
                  className="card-img-top"
                  alt="..."
                ></img>
                <p>
                  Bicicleta de velocidad
                </p>
                <p>
                  Precio:$1.200.900
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <div className="card-producto">
                <img
                  src="https://cdn.pixabay.com/photo/2019/07/27/18/24/cyclist-4367308_960_720.jpg"
                  className="card-img-top"
                  alt="..."
                ></img>
                <p>
                  casco amateur
                </p>
                <p>
                  Precio:$16.800
                </p>
              </div>
            </div>
            <div class="carousel-item">
              <div className="card-producto">
                <img
                  src="https://cdn.pixabay.com/photo/2020/01/16/06/24/activity-4769731_960_720.jpg"
                  className="card-img-top"
                  alt="..."
                ></img>
              <p>
                  casco profesional
                </p>
                <p>
                  Precio:$36.800
                </p>
                
              </div>
            </div>
            <div class="carousel-item">
              <div className="card-producto">
                <img
                  src="https://cdn.pixabay.com/photo/2015/12/06/18/28/capsules-1079838_960_720.jpg"
                  className="card-img-top"
                  alt="..."
                ></img>
              <p>
                  aminoacidos
                </p>
                <p>
                  Precio:$8.800
                </p>
                
              </div>
            </div>
            <div class="carousel-item">
              <div className="card-producto">
                <img
                  src="https://cdn.pixabay.com/photo/2016/09/01/14/20/chocolate-bar-1636220_1280.jpg"
                  className="card-img-top"
                  alt="..."
                ></img>
              <p>
                  barra proteian
                </p>
                <p>
                  Precio:$6.800
                </p>
                
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

        <button
          onClick={() => alert("proximamente")}
          type="submit"
          className="btn btn-dark"
        >
          Agregar al carro
        </button>
      </div>
    </form>
  );
};
