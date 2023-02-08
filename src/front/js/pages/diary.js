import React from "react";
import { Footer } from "./diaryContact/Footer";
import { Navbar } from "./diaryContact/Navbar";
import { Index } from "./diaryContact/Pages";

export const Diary= () => {
  return (
    <form className="contenedor-login">
      
      <Navbar />
			<Index />
			<Footer />
    </form>
  );
};