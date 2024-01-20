import _ from "lodash";
import { Image, Input, Row } from "antd";
import LandingImage from "../../images/landing-image.jpeg";
import ProductCard from "./ProductItem";
import { useState } from "react";
import { ProductItem } from "../types/types";

const dummyProducts: ProductItem[] = [
  {
    id: 1,
    label: "Yam Yam Chocolate Flavour",
    measureField: "50g",
    imageUrl: [
      "https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/297756_XL1_20210505.jpg",
      "https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=900/app/images/products/sliding_image/120179a.jpg?ts=1690813377",
    ],
    merchants: [
      {
        name: "ntuc",
        price: 1.2,
        offer: "Buy 3 get 1 Free",
        link: "https://www.google.com",
      },
      {
        name: "coldstorage",
        price: 1.4,
        link: "https://www.google.com",
      },
    ],
  },
  {
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
        link: "https://www.google.com",
      },
    ],
  },
  {
    id: 3,
    label: "Fairprice Potato Chips - Spicy",
    measureField: "92g",
    imageUrl: [
      "https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/13207649_XL1_20211103.jpg?w=1200&q=70",
    ],
    merchants: [
      {
        name: "ntuc",
        price: 1.0,
        link: "https://www.google.com",
      },
    ],
  },
  {
    id: 4,
    label: "Yuan Zhen Yuan Enoki Mushroom Thailand",
    measureField: "200g",
    imageUrl: [
      "https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/90187028_XL1_20231201.jpg?w=1200&q=70",
      "https://coldstorage.com.sg/vcpimg/thumb/5016758%20Taiwan%20Enoki.jpg",
    ],
    merchants: [
      {
        name: "ntuc",
        price: 1.51,
        link: "https://www.google.com",
      },
      {
        name: "coldstorage",
        price: 1.5,
        link: "https://www.google.com",
      },
    ],
  },
  {
    id: 5,
    label: "Yam Yam Chocolate Flavour",
    measureField: "50g",
    imageUrl: [
      "https://media.nedigital.sg/fairprice/fpol/media/images/product/XL/297756_XL1_20210505.jpg",
      "https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=900/app/images/products/sliding_image/120179a.jpg?ts=1690813377",
    ],
    merchants: [
      {
        name: "ntuc",
        price: 1.2,
        offer: "Buy 3 get 1 Free",
        link: "https://www.google.com",
      },
      {
        name: "coldstorage",
        price: 1.4,
        link: "https://www.google.com",
      },
    ],
  },
];

const LandingContent = () => {
  const [inputValue, setInputValue] = useState<string>("");
  const [filteredProducts, setFilteredProducts] =
    useState<ProductItem[]>(dummyProducts);
  const inputChangeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
    const input = event.target.value;
    setInputValue(input);
    setFilteredProducts(filterProducts(input));
  };

  const filterProducts = (input: string) => {
    return _.filter(
      dummyProducts,
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
      <Row style={{ width: "100%", height: "100%" }}>
        {filteredProducts.map((product, index) => (
          <ProductCard product={product} key={index} />
        ))}
      </Row>
    </Row>
  );
};

export default LandingContent;
