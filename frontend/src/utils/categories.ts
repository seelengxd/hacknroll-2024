import { ItemType, MenuItemType } from "antd/es/menu/hooks/useItems";

export const categories: ItemType<MenuItemType>[] = [
  { key: "fruits", label: "Fruits" },
  { key: "vegetable", label: "Vegetable" },
  { key: "snacks", label: "Snacks" },
];
