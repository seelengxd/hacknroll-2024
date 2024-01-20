import { MerchantNameMap } from "../../utils/utils";
import { MerchantName } from "../types/types";

type LogoProps = {
  name: MerchantName;
};

const LogoAvailability = ({ name }: LogoProps) => {
  return MerchantNameMap[name].image;
};

export default LogoAvailability;
