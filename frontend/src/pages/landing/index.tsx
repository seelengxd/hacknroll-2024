import { Layout } from "antd";
import { Footer, Header } from "antd/es/layout/layout";
import LandingContent from "./Content";
import HomeLogo from "../common/HomeLogo";

const Landing = () => {
  return (
    <Layout>
      <Header
        style={{
          position: "sticky",
          top: 0,
          zIndex: 3,
          width: "100%",
          display: "flex",
          alignItems: "center",
        }}
      >
        <HomeLogo />
      </Header>
      <LandingContent />
      <Footer style={{ textAlign: "center" }}>
        Ant Design ©{new Date().getFullYear()} Created by Ant UED
      </Footer>
    </Layout>
  );
};

export default Landing;
