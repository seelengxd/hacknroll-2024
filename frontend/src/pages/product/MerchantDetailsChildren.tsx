import { Button, Typography } from "antd";
import { MerchantDetailChildrenProps } from "../types/types";

const MerchantDetailsChildren = ({ merchant }: MerchantDetailChildrenProps) => {
  return (
    <>
      <div
        style={{
          paddingBottom: 8,
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        <Button
          href={merchant.link}
          target="_blank"
          style={{ backgroundColor: "#1A43BF", color: "#fff" }}
        >
          Product Link
        </Button>
        {`$${merchant.price}`}
      </div>
      {merchant.offer && (
        <Typography.Paragraph>{merchant.offer}</Typography.Paragraph>
      )}
    </>
  );
};

export default MerchantDetailsChildren;
