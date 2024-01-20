import { MerchantMapType } from "../pages/types/types";
import NTUCImage from "../images/ntuc-logo.png";
import ColdStorageImage from "../images/cold-storage-logo.png";
import ShengSiongImage from "../images/shengsiong-logo.png";
import UnknownImage from "../images/unknown-logo.jpg";

const LogoSize = 24;

const NTUCLogo = () => {
  return (
    <img
      width={LogoSize}
      height={LogoSize}
      src={NTUCImage}
      alt={UnknownImage}
    />
  );
};

const ColdStorageLogo = () => {
  return (
    <img
      width={LogoSize}
      height={LogoSize}
      src={ColdStorageImage}
      alt={UnknownImage}
    />
  );
};

const ShengSiongLogo = () => {
  return (
    <img
      width={LogoSize}
      height={LogoSize}
      src={ShengSiongImage}
      alt={UnknownImage}
    />
  );
};

export const MerchantNameMap: MerchantMapType = {
  NTUC: { label: "FairPrice", image: <NTUCLogo /> },
  "Cold Storage": { label: "Cold Storage", image: <ColdStorageLogo /> },
  "Sheng Siong": { label: "Sheng Siong", image: <ShengSiongLogo /> },
  RedMart: { label: "RedMart", image: <ShengSiongLogo /> },
};
