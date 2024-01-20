import { Navigate, Route, Routes } from "react-router-dom";
import Landing from "./pages/landing";
import Product from "./pages/product";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

function App() {
  const queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryClient}>
      <div className="App">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/product/:id" element={<Product />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </QueryClientProvider>
  );
}

export default App;
