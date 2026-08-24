import argparse

def build_wos_query(keywords, field_code="TS", operator="AND", near=None):
    """
    Builds a Web of Science search query.
    
    Args:
        keywords (list): List of search terms.
        field_code (str): WOS field code (e.g., TS=Topic, TI=Title, AU=Author, OG=Organization).
        operator (str): Boolean operator (AND, OR, NOT) or NEAR.
        near (int): Proximity range for NEAR operator.
    
    Returns:
        str: Formatted WOS query string.
    """
    if not keywords:
        return ""
    
    if operator.upper() == "NEAR":
        op_str = f" NEAR/{near} " if near else " NEAR "
    else:
        op_str = f" {operator.upper()} "
    
    # Handle phrases with spaces
    processed_keywords = []
    for kw in keywords:
        if " " in kw and not (kw.startswith('"') and kw.endswith('"')):
            processed_keywords.append(f'"{kw}"')
        else:
            processed_keywords.append(kw)
    
    query = op_str.join(processed_keywords)
    return f"{field_code}=({query})"

def main():
    parser = argparse.ArgumentParser(description="WOS Query Builder Utility")
    parser.add_argument("keywords", nargs="+", help="Keywords to search for")
    parser.add_argument("--field", default="TS", help="Field code (default: TS for Topic)")
    parser.add_argument("--op", default="AND", choices=["AND", "OR", "NOT", "NEAR"], help="Operator (default: AND)")
    parser.add_argument("--near", type=int, help="Proximity for NEAR operator")
    
    args = parser.parse_args()
    
    query = build_wos_query(args.keywords, args.field, args.op, args.near)
    print(f"\nGenerated Web of Science Query:\n{query}\n")

if __name__ == "__main__":
    main()
