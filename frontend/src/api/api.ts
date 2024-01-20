const apiEndpoint = process.env.REACT_APP_MY_API_KEY ?? "http://127.0.0.1:5000";

export const getItems = () =>
  fetch(apiEndpoint + "/items").then((res) => res.json());

export const getItem = (id: number) =>
  fetch(`${apiEndpoint}/items/${id}`).then((res) => res.json());
