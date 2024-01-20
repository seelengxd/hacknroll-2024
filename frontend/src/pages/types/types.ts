export type ProductItem = {
  id: number;
  label: string;
  measureField: string;
  imageUrl: string[];
  merchants: Merchant[];
};

export type Merchant = {
  name: MerchantName;
  price: number;
  offer?: string;
  link: string;
};

export type MerchantName = "NTUC" | "Cold Storage" | "Sheng Siong" | "RedMart";

export type MerchantMapType = {
  [key in MerchantName]: MerchantType;
};

type MerchantType = {
  label: string;
  image: JSX.Element;
};

export interface MerchantDetailChildrenProps {
  merchant: Merchant;
}
