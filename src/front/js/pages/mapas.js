import React, { pages } from "react";
import  GoogleMaps from "simple-react-google-maps";

export const Mapas =() =>{
    return(
        <div className="container">
            <GoogleMaps
            apiKey= {("AIzaSyCS3Frzif9t39ykB4WlbAipLjJ7uQeOxTg")}
            style={{height : "500px", width: "290px"}}
            zoom={15}
            center={{
                lat: -33.5070426,
                lng: -70.6609057,
            }}
         />
        </div>
    )
}
