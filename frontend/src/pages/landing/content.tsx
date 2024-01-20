import _ from "lodash";
import { Image, Input, Row, Spin } from "antd";
import LandingImage from "../../images/landing-image.jpeg";
import ProductCard from "./ProductCard";
import { useEffect, useState } from "react";
import { ProductItem } from "../types/types";
import { useQuery } from "@tanstack/react-query";
import { getItems } from "../../api/api";
import NoData from "./NoData";

const LandingContent = () => {
  const { isLoading, error, data } = useQuery({
    queryKey: ["getItems"],
    queryFn: getItems,
  });

  if (error) {
    console.error(error);
  }

  useEffect(() => {
    if (data === undefined) return;
    setFilteredProducts(data.data);
  }, [data]);

  const [inputValue, setInputValue] = useState<string>("");
  const [filteredProducts, setFilteredProducts] = useState<ProductItem[]>([]);
  const inputChangeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
    const input = event.target.value;
    setInputValue(input);
    setFilteredProducts(filterProducts(input));
  };

  console.log(filteredProducts);

  const filterProducts = (input: string) => {
    return _.filter(
      data.data,
      (product) =>
        product.label.toLowerCase().includes(input.toLowerCase()) ||
        (input.toLowerCase() === "offer" &&
          _.some(product.merchants, (m) => _.has(m, "offer")))
    );
  };

  return (
    <Row gutter={[0, 24]}>
      <Image
        style={{ objectFit: "contain" }}
        height={300}
        width={"100%"}
        src={LandingImage}
      />
      <div style={{ display: "flex", justifyContent: "center", width: "100%" }}>
        <Input
          style={{ width: "80%" }}
          placeholder="Search Product"
          onChange={inputChangeHandler}
          value={inputValue}
        />
      </div>
      {isLoading ? (
        <Spin />
      ) : filteredProducts.length === 0 ? (
        <NoData />
      ) : (
        <Row style={{ width: "100%", height: "100%" }}>
          {filteredProducts.map((product, index) => (
            <ProductCard product={product} key={index} />
          ))}
        </Row>
      )}
    </Row>
  );
};

export default LandingContent;
