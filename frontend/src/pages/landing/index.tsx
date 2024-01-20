import { Layout } from "antd";
import { Footer } from "antd/es/layout/layout";
import LandingContent from "./content";
import Navbar from "../common/Navbar";

const Landing = () => {
  return (
    <Layout>
      <Navbar />
      <LandingContent />
      <Footer style={{ textAlign: "center" }}>
        Hack&Roll ©{2024} Created by Team ?
      </Footer>
    </Layout>
  );
};

export default Landing;
