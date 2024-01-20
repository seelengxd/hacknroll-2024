const apiEndpoint = process.env.REACT_APP_MY_API_KEY ?? "http://127.0.0.1:5000";

export const getItems = async () => {
  try {
    const response = await fetch(`${apiEndpoint}/items`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching item:", error);
    throw error;
  }
};

export const getItem = async (id: number) => {
  try {
    const response = await fetch(`${apiEndpoint}/items/${id}`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching item:", error);
    throw error;
  }
};

export const searchItems = async (input: string, pageNumber: number) => {
  let url = `${apiEndpoint}/search?page=${pageNumber}`;
  if (input !== "") {
    url += `&q=${encodeURIComponent(input)}`;
  }

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
};
