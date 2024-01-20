import { Pagination, Row } from "antd";
import { ProductItem } from "../types/types";
import ProductCard from "./ProductCard";

interface ProductsProps {
  filteredProducts: ProductItem[];
  currentPageNumber: number;
  totalItems: number;
  setPageNumber: (page: number) => void;
}

const Products = ({
  filteredProducts,
  currentPageNumber,
  totalItems,
  setPageNumber,
}: ProductsProps) => {
  return (
    <>
      <Row style={{ width: "100%", height: "100%" }}>
        {filteredProducts.map((product, index) => (
          <ProductCard product={product} key={index} />
        ))}
      </Row>
      <Pagination
        current={currentPageNumber}
        onChange={(page) => setPageNumber(page)}
        defaultPageSize={30}
        total={totalItems}
      />
    </>
  );
};

export default Products;
