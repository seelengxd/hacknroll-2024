import { Layout } from "antd";
import { Footer } from "antd/es/layout/layout";
import ProductContent from "./content";
import Navbar from "../common/Navbar";

const Product = () => {
  return (
    <Layout>
      <Navbar />
      <ProductContent />
      <Footer style={{ textAlign: "center" }}>
        Hack&Roll ©{2024} Created by Team ?
      </Footer>
    </Layout>
  );
};

export default Product;
