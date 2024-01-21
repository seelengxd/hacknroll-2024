import Icon from "@ant-design/icons/lib/components/Icon";
import { useNavigate } from "react-router-dom";
import { ReactComponent as HomeSVG } from "../../images/home-logo.svg";

const HomeLogo = () => {
  const navigate = useNavigate();
  const fontStyle = {
    fontFamily: "'Comic Sans MS', cursive",
    color: "#fff",
  };
  return (
    <>
      <Icon
        component={HomeSVG}
        style={{ backgroundColor: "#ffffff", fontSize: 32, marginRight: 8 }}
      />
      <div onClick={() => navigate("/")} style={fontStyle}>
        Price Chop Chop
      </div>
    </>
  );
};

export default HomeLogo;
