import {
  Button,
  Carousel,
  Col,
  Collapse,
  CollapseProps,
  Image,
  Row,
  Typography,
} from "antd";
import { Merchant, ProductItem } from "../types/types";
import _ from "lodash";
import { MerchantNameMap } from "../../utils/utils";

const dummyProduct: ProductItem = {
  id: 2,
  label: "Wang Wang",
  measureField: "92g",
  imageUrl: [
    "https://assets.lyreco.com/is/image/lyrecows/2018-13235431?locale=SG_en&id=VXFq51&fmt=jpg&dpr=off&fit=constrain,1&wid=430&hei=430",
    "https://img.ws.mms.shopee.sg/26c47d8c291de922a082b09b2540e306",
  ],
  merchants: [
    {
      name: "ntuc",
      price: 1.8,
      offer: "Buy 3 and get 1 FREE!",
      link: "https://www.google.com",
    },
    {
      name: "coldstorage",
      price: 1.4,
      link: "https://www.google.com",
    },
    {
      name: "shengsiong",
      price: 1.8,
      offer: "Buy 2 and get 50% OFF on the 3rd",
      link: "https://www.google.com",
    },
  ],
};

const ProductContent = () => {
  // Fetch Product by ID (TO BE IMPLEMENTED)

  const product = dummyProduct;

  return (
    <Row>
      <Col span={12}>
        <Carousel>
          {product.imageUrl.map((url, index) => (
            <Image key={index} src={url} width={"100%"} />
          ))}
        </Carousel>
      </Col>
      <Col span={12}>
        <div style={{ margin: 30 }}>
          <Typography.Title>{product.label}</Typography.Title>
          <Typography.Text>{`Measured Unit: ${product.measureField}`}</Typography.Text>
          <MerchantDetails merchants={product.merchants} />
        </div>
      </Col>
    </Row>
  );
};

interface MerchantDetailsProps {
  merchants: Merchant[];
}

const MerchantDetails = ({ merchants }: MerchantDetailsProps) => {
  const merchantsToCollapseItems = (
    merchants: Merchant[]
  ): CollapseProps["items"] => {
    return _.map(merchants, (m) => ({
      key: m.name,
      label: <MerchantLabel merchant={m} />,
      children: <MerchantDetailsChildren merchant={m} />,
      extra: <div>{`${m.price} / unit`}</div>,
    }));
  };

  return (
    <div style={{ marginTop: 12 }}>
      <Collapse items={merchantsToCollapseItems(merchants)} />
    </div>
  );
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
      <div style={{ paddingBottom: 8 }}>
        <Button
          href={merchant.link}
          target="_blank"
          style={{ backgroundColor: "#1A43BF", color: "#fff" }}
        >
          Product Link
        </Button>
      </div>
      {merchant.offer && (
        <Typography.Paragraph>{merchant.offer}</Typography.Paragraph>
      )}
    </>
  );
};

export default ProductContent;
