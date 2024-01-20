import {
  Button,
  Carousel,
  Col,
  Collapse,
  CollapseProps,
  Image,
  Row,
  Spin,
  Tag,
  Typography,
} from "antd";
import { Merchant, ProductItem } from "../types/types";
import _ from "lodash";
import { MerchantNameMap } from "../../utils/utils";
import { useQuery } from "@tanstack/react-query";
import { getItem } from "../../api/api";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import NoData from "../landing/NoData";

const ProductContent = () => {
  // Fetch Product by ID (TO BE IMPLEMENTED)
  const location = useLocation();
  const pathName = location.pathname.split("/");
  const productId =
    pathName.length !== 0 ? Number(pathName[pathName.length - 1]) : -1;

  const { isLoading, error, data } = useQuery({
    queryKey: ["getItem"],
    queryFn: () => getItem(productId),
  });

  if (error) {
    console.error(error);
  }

  useEffect(() => {
    if (data === undefined) return;
    setProduct(data.data);
  }, [data]);

  const [product, setProduct] = useState<ProductItem>();

  return (
    <Row>
      {isLoading ? (
        <Spin />
      ) : (
        <>
          <Col span={12}>
            <Carousel>
              {product &&
                product.imageUrl.map((url, index) => (
                  <Image key={index} src={url} width={"100%"} />
                ))}
            </Carousel>
          </Col>
          <Col span={12}>
            <div style={{ margin: 30 }}>
              {product && (
                <>
                  <Typography.Title>{product.label}</Typography.Title>
                  <Typography.Text>{`Measured Unit: ${product.measureField}`}</Typography.Text>
                  <MerchantDetails merchants={product.merchants} />
                </>
              )}
            </div>
          </Col>
          {!product && <NoData />}
        </>
      )}
    </Row>
  );
};

interface MerchantDetailsProps {
  merchants: Merchant[];
}

const MerchantDetails = ({ merchants }: MerchantDetailsProps) => {
  const mostAffordableMerchant = merchants.sort(
    (m1, m2) => m1.price - m2.price
  )[0].name;

  const merchantsToCollapseItems = (
    merchants: Merchant[]
  ): CollapseProps["items"] => {
    return _.map(merchants, (m) => ({
      key: m.name,
      label: <MerchantLabel merchant={m} />,
      children: <MerchantDetailsChildren merchant={m} />,
      extra: mostAffordableMerchant == m.name ? <MostAffordableTag /> : null,
    }));
  };

  return (
    <div style={{ marginTop: 12 }}>
      <Collapse
        items={merchantsToCollapseItems(merchants)}
        defaultActiveKey={[mostAffordableMerchant]}
      />
    </div>
  );
};

const MostAffordableTag = () => {
  return <Tag color="#87d068">Most Affordable</Tag>;
};

interface MerchantDetailChildrenProps {
  merchant: Merchant;
}

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

export default ProductContent;
