const getState = ({ getStore, getActions, setStore }) => {
  const url = process.env.BACKEND_URL;
  return {
    store: {
      user: {
        type: "",
        token: "",
        id: "",
      },
    },
    actions: {
      login: async (dataUser) => {
        const response = await fetch(url + "/api/login", {
          crossDomain: true,
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
          },
          referrerPolicy: "no-referrer",
          body: JSON.stringify(dataUser),
        }).then((response) => response.json());

        if (response["code"] >= 2) {
          console.log(response["response"]);
        } else {
          let responseUser = {
            type: response["type"],
            id: response["id"],
            token: response["token"],
          };
          setStore({user:responseUser})
          localStorage.setItem("iProBike-token", responseUser.token);
          localStorage.setItem("iProBike-type", responseUser.type);

          console.log(getStore.user); //<-- comprobar datos
        }
      },
    },
  };
};

export default getState;
