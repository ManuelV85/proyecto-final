import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import { Home } from "./pages/home";

import injectContext from "./store/appContext";

import { Footer } from "./component/footer";
import { Login } from "./pages/Login";
import { Registration } from "./pages/Registration";
import { Biker } from "./pages/inicio_biker";
import { Sos } from "./pages/sos";
import { UserStore } from "./pages/userState";

import { MenuStore } from "./pages/inicio_Store.js";
import { Upload_item } from "./pages/Upload";
import Listadetareas from "./pages/listatareas";
import { Tableinventary } from "./pages/tablaInventary";
import { Emailpassword } from "./pages/email.password";
import { Horario } from "./pages/horario";
import { Page404 } from "./pages/page404";
import { Diary } from "./pages/diary"
import { Travel } from "./pages/Travel";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div className="app">
      <div ClassName="container">
        <BrowserRouter basename={basename}>
          <Routes>
            <Route element={<Home />} path="/" />
            <Route element={<Login />} path="/login" />
            <Route element={<Registration />} path="/registration" />
            <Route element={<Biker />} path="/biker" />
            <Route element={<UserStore />} path="/userstore" />
            <Route element={<MenuStore />} path="/menustore" />
            <Route element={<Upload_item />} path="/upload_item" />
            <Route element={<Tableinventary />} path="/tableinventary" />
            <Route element={<Emailpassword />} path="/emailpassword" />
            <Route element={<Sos/>} path="/sos" />
            <Route element={<Horario/>} path="/horario" />
            <Route element={<Page404/>} path="/page404" />
            <Route element={<Diary/>} path="/diary"/>
            <Route element={<Travel/>} path="/travel"/>

          </Routes>
        </BrowserRouter>
      </div>
    </div>
  );
};

export default injectContext(Layout);
