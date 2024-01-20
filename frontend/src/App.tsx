import { Navigate, Route, Routes } from "react-router-dom";
import Landing from "./pages/landing";
import Product from "./pages/product";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/product/:id" element={<Product />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </div>
  );
}

export default App;
