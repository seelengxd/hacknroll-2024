import { Header } from "antd/es/layout/layout";
import HomeLogo from "./HomeLogo";

const Navbar = () => {
  return (
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
  );
};

export default Navbar;
