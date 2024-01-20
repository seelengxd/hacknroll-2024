import { Layout } from "antd";
import { Footer, Header } from "antd/es/layout/layout";
import HomeLogo from "../common/HomeLogo";
import ProductContent from "./content";

const Product = () => {
  return (
    <Layout>
      <Header
        style={{
          position: "sticky",
          top: 0,
          zIndex: 1,
          width: "100%",
          display: "flex",
          alignItems: "center",
        }}
      >
        <HomeLogo />
      </Header>
      <ProductContent />
      <Footer style={{ textAlign: "center" }}>
        Ant Design ©{new Date().getFullYear()} Created by Ant UED
      </Footer>
    </Layout>
  );
};

export default Product;
