from typing import List, Dict

class FoodItem:
    def __init__(self, name: str, expiry_date: str, category: str):
        self.name = name
        self.expiry_date = expiry_date
        self.category = category

class FoodManager:
    def __init__(self):
        self.items: List[FoodItem] = []
    
    def add_item(self, name: str, expiry_date: str, category: str):
        """เพิ่มรายการอาหารใหม่"""
        new_item = FoodItem(name, expiry_date, category)
        self.items.append(new_item)
        print(f"เพิ่ม '{name}' สำเร็จแล้ว")
    
    def show_all_items(self):
        """แสดงรายการอาหารทั้งหมด"""
        if not self.items:
            print("ยังไม่มีรายการอาหาร")
            return
        
        print("\nรายการอาหารทั้งหมด:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} | หมดอายุ: {item.expiry_date} | ประเภท: {item.category}")
    
    def remove_item(self, item_index: int):
        """ลบรายการอาหารตามลำดับที่ระบุ"""
        if 1 <= item_index <= len(self.items):
            removed_item = self.items.pop(item_index - 1)
            print(f"ลบ '{removed_item.name}' เรียบร้อยแล้ว")
        else:
            print("ลำดับไม่ถูกต้อง")
    
    def summarize_items(self):
        """สรุปจำนวนอาหารแต่ละประเภท"""
        if not self.items:
            print("ยังไม่มีรายการอาหาร")
            return
        
        category_counts: Dict[str, int] = {}
        for item in self.items:
            category_counts[item.category] = category_counts.get(item.category, 0) + 1
        
        print("\nสรุปจำนวนอาหารแต่ละประเภท:")
        for category, count in category_counts.items():
            print(f"- {category}: {count} รายการ")

def display_food_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*40)
    print("ระบบจัดการเมนูอาหารและวัตถุดิบ")
    print("="*40)
    print("1. เพิ่มรายการอาหาร")
    print("2. แสดงรายการทั้งหมด")
    print("3. ลบรายการอาหาร")
    print("4. สรุปจำนวนอาหารตามประเภท")
    print("5. ออกจากระบบ")
    print("="*40)

def main():
    manager = FoodManager()
    
    while True:
        display_food_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        if choice == "1":
            name = input("ชื่อรายการอาหาร: ")
            expiry_date = input("วันที่หมดอายุ (dd/mm/yyyy): ")
            category = input("ประเภทอาหาร (เนื้อสัตว์/ผัก/ผลไม้/อื่นๆ): ")
            manager.add_item(name, expiry_date, category)
        
        elif choice == "2":
            manager.show_all_items()
        
        elif choice == "3":
            manager.show_all_items()
            if manager.items:
                try:
                    item_num = int(input("ลำดับรายการที่ต้องการลบ: "))
                    manager.remove_item(item_num)
                except ValueError:
                    print("กรุณาป้อนตัวเลขเท่านั้น")
        
        elif choice == "4":
            manager.summarize_items()
        
        elif choice == "5":
            print("\nขอบคุณที่ใช้บริการระบบจัดการเมนูอาหาร!")
            break
        
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()
    