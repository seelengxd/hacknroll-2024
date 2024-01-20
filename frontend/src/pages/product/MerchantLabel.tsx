import { Typography } from "antd";
import { MerchantNameMap } from "../../utils/utils";
import { MerchantDetailChildrenProps } from "../types/types";

const MerchantLabel = ({ merchant }: MerchantDetailChildrenProps) => {
  const mappedMerchant = MerchantNameMap[merchant.name];

  return (
    <div
      style={{ display: "flex", justifyContent: "start", alignItems: "center" }}
    >
      {mappedMerchant.image}
      <div style={{ margin: "0 8px" }}>{mappedMerchant.label}</div>
      {merchant.offer && (
        <Typography.Text
          style={{
            backgroundColor: "#FFA500",
            color: "#fff",
            fontSize: 10,
            padding: "2px 6px",
            borderRadius: 2,
          }}
        >
          Offer
        </Typography.Text>
      )}
    </div>
  );
};

export default MerchantLabel;
