import _ from "lodash";
import { ProductProps } from "./ProductCard";
import LogoAvailability from "./LogoAvailability";

const CardDescription = ({ product }: ProductProps) => {
  const lowestPrice = Math.min(..._.map(product.merchants, (m) => m.price));
  const availableMerchantNames = _.uniq(
    _.map(product.merchants, (m) => m.name)
  );

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

export default CardDescription;
