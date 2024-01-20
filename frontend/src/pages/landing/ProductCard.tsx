import _ from "lodash";
import { Card, Carousel, Col, Image, Typography } from "antd";
import Meta from "antd/es/card/Meta";

import { MerchantName, ProductItem } from "../types/types";
import { MerchantNameMap } from "../../utils/utils";
import { useNavigate } from "react-router-dom";

type Props = {
  product: ProductItem;
};

type LogoProps = {
  name: MerchantName;
};

const ProductCard = ({ product }: Props) => {
  const navigate = useNavigate();
  const hasOffer = _.some(product.merchants, (m) => _.has(m, "offer"));

  return (
    <Col style={{ width: 300, height: 400, position: "relative", margin: 12 }}>
      <Card
        hoverable
        style={{ width: 300, position: "absolute" }}
        cover={
          <Carousel autoplay>
            {product.imageUrl.map((url, index) => (
              <Image
                key={index}
                src={url}
                alt={"Image Not Found"}
                height={300}
              />
            ))}
          </Carousel>
        }
        actions={[]}
        onClick={() => navigate(`product/${product.id}`)}
      >
        <Meta
          title={product.label}
          description={<CardDescription product={product} />}
        />
      </Card>
      {hasOffer && (
        <Typography.Text
          style={{
            backgroundColor: "#FFA500",
            position: "absolute",
            top: 10,
            right: 8,
            color: "#FFF",
            fontSize: 14,
            zIndex: 2,
            padding: "0 8px",
            borderRadius: "4px",
          }}
        >
          Offer
        </Typography.Text>
      )}
    </Col>
  );
};

const CardDescription = ({ product }: Props) => {
  const lowestPrice = Math.min(..._.map(product.merchants, (m) => m.price));
  const availableMerchantNames = _.map(product.merchants, (m) => m.name);

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <div>
        {availableMerchantNames.map((n) => (
          <LogoAvailability name={n} key={n} />
        ))}
      </div>
      <div>{`Lowest @$${lowestPrice}`}</div>
    </div>
  );
};

const LogoAvailability = ({ name }: LogoProps) => {
  return MerchantNameMap[name].image;
};

export default ProductCard;
