import { Button, Image, Input, Row, Spin } from "antd";
import LandingImage from "../../images/landing-image.jpeg";
import { useEffect, useState } from "react";
import { ProductItem } from "../types/types";
import { useQuery } from "@tanstack/react-query";
import { searchItems } from "../../api/api";
import NoData from "./NoData";
import { SearchOutlined } from "@ant-design/icons";
import Products from "./Products";

const LandingContent = () => {
  const [inputValue, setInputValue] = useState<string>("");
  const [filteredInput, setFilteredInput] = useState<string>("");
  const [products, setProducts] = useState<ProductItem[]>([]);
  const inputChangeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
    const input = event.target.value;
    setInputValue(input);
  };

  const searchProductHandler = (input: string) => {
    setPageNumber(1);
    setFilteredInput(input);
  };
  const [pageNumber, setPageNumber] = useState<number>(1);
  const [totalItems, setTotalItems] = useState<number>(-1);

  const { isLoading, error, data } = useQuery({
    queryKey: ["searchItems", filteredInput, pageNumber],
    queryFn: () => searchItems(filteredInput, pageNumber),
  });

  if (error) {
    console.error(error);
  }

  useEffect(() => {
    if (data === undefined) return;
    setProducts(data.data);
    setTotalItems(data.total_results);
  }, [data]);

  return (
    <Row gutter={[0, 24]}>
      <Image
        style={{ objectFit: "fill" }}
        height={300}
        width={"100%"}
        src={LandingImage}
      />
      <div style={{ display: "flex", justifyContent: "center", width: "100%" }}>
        <Input
          style={{ width: "70%", marginTop: -48, borderRadius: 10 }}
          placeholder="Search Product..."
          onChange={inputChangeHandler}
          value={inputValue}
          suffix={
            <Button
              onClick={() => searchProductHandler(inputValue)}
              style={{
                borderRadius: 10,
                backgroundColor: "#1A43BF",
                color: "#fff",
              }}
            >
              Search
              <SearchOutlined style={{ color: "#fff" }} />
            </Button>
          }
        />
      </div>
      {isLoading ? (
        <Spin />
      ) : setProducts.length === 0 ? (
        <NoData />
      ) : (
        <Products
          filteredProducts={products}
          currentPageNumber={pageNumber}
          setPageNumber={setPageNumber}
          totalItems={totalItems}
        />
      )}
    </Row>
  );
};

export default LandingContent;
