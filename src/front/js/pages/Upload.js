import React from "react";
import { useForm } from "react-hook-form";

export const Upload_item = () => {
  const url = process.env.BACKEND_URL;
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (dataUser) => {
    
    var data = new FormData();
    console.log(dataUser["picture"][0]);
    data.append("category", dataUser["category"]);
    data.append("product", dataUser["product"]);
    data.append("price", dataUser["price"]);
    data.append("description", dataUser["description"]);
    data.append("picture", dataUser["picture"][0]);
    data.append("user_id", 1);
    console.log(data);
    for (var pair of data.entries()) {
      console.log(pair[0] + ", " + pair[1]);
    }

    const response = await fetch(
      url + `/api/users/inventory`,

      {
        crossDomain: true,
        method: "POST",
        mode: "cors",
        // headers: {
        // "Content-Type": "multipart/form-data", //permite subir no solo json
        //},
        referrerPolicy: "no-referrer",
        body: data,
      }
    ).then((response) => response.json());
    if (response["code"] == 1) {
      alert(response["response"]);
    } else if (response["code"] == 0) alert(response["response"]);
  };

  return (
    <form
      enctype="multipart/form-data"
      onSubmit={handleSubmit(onSubmit)}
      className="contenedor-login"
    >
      <div className="mb-3">
        <select
          class="form-select"
          aria-label="Default select example"
          {...register("category")}
        >
          <option selected>Categorias</option>
          <option value="Accesorios">Accesorios</option>
          <option value="Repuestos">Repuestos</option>
          <option value="Indumentaria">Indumentaria</option>
          <option value="Bicicletas">Bicicletas</option>
        </select>
        <label for="exampleInputEmail1" className="form-label">
          Producto{" "}
        </label>
        <input
          type="text"
          className="form-control"
          id="InputProducto"
          aria-describedby="emailHelp"
          placeholder="ingrese nombre producto"
          {...register("product")}
        />

        <label for="InputEmail1" className="form-label">
          Precio Unitario (CLP){" "}
        </label>
        <input
          type="text"
          className="form-control"
          id="monto"
          aria-describedby="emailHelp"
          placeholder="ej:15000"
          {...register("price")}
          onChange={(e) => {
            let monto = e.target.value;
            monto = monto.replace(/[^0-9]/g, "");
            const formatter = new Intl.NumberFormat("es-CL", {
              style: "currency",
              currency: "CLP",
            });
            const montoFormateado = formatter.format(monto);
            e.target.value = montoFormateado;
          }}
        />

        <div className="mb-3">
          <label for="FormControlTextarea1" class="form-label">
            Descripcion del producto
          </label>
          <textarea
            class="form-control"
            id="FormControlTextarea1"
            {...register("description")}
            rows="2"
          ></textarea>
        </div>
        <div className="cargar-imagen"></div>

        <input
          type="file"
          id="my-button"
          name=""
          {...register("picture")}
          accept="image/png,image/jpg"
        ></input>
        <button
          type="submit"
          className="btn btn-dark"
          onClick={() => navigate("/menustore")}
        >
          Guardar
        </button>
      </div>
    </form>
  );
};