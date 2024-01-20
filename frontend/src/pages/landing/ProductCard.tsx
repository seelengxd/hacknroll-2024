import _ from "lodash";
import { Card, Carousel, Col, Image, Typography } from "antd";
import Meta from "antd/es/card/Meta";

import { ProductItem } from "../types/types";
import { useNavigate } from "react-router-dom";
import CardDescription from "./CardDescription";

export type ProductProps = {
  product: ProductItem;
};

const ProductCard = ({ product }: ProductProps) => {
  const navigate = useNavigate();
  const hasOffer = _.some(
    product.merchants,
    (m) => m.offer !== null && _.has(m, "offer")
  );

  return (
    <Col style={{ width: 300, height: 400, position: "relative", margin: 12 }}>
      <Card
        hoverable
        style={{ width: 300, position: "absolute" }}
        cover={
          <Carousel autoplay>
            {product.imageUrl?.map((url, index) => (
              <Image
                key={index}
                src={url}
                alt={"Image Not Found"}
                height={300}
              />
            )) ?? []}
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

export default ProductCard;
