---
description: "Run investment calculations — BRRRR, flip, buy-and-hold, seller finance note, cash-on-cash, and creative finance scenarios."
argument-hint: "[strategy: brrrr|flip|hold|seller-finance|subto|wrap|note-creation] [--price amount] [--arv amount] [--rent amount] [--rehab amount] [--rate percentage] [--term years]"
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebSearch, TodoWrite]
---

# Investment Calculator

The user wants to run detailed investment calculations for a specific real estate or creative finance strategy.

**Arguments provided:** $ARGUMENTS

## Step-by-Step Execution

### Step 0: Parse Arguments
- Extract the investment strategy
- Extract financial inputs:
  - `--price` — purchase price
  - `--arv` — after repair value
  - `--rent` — monthly rent
  - `--rehab` — renovation budget
  - `--rate` — interest rate (for financing)
  - `--term` — loan term in years
  - `--down` — down payment or cash invested
- If missing critical inputs, ask the user for the numbers

### Step 1: Load T.O.P. Method Context
- Read `~/.claude/brain/knowledge-base/top-method/03-underwriting-how-deals-get-scored.md`
- Read `~/.claude/brain/knowledge-base/top-method/06-fee-structure-deep-dive.md`
- Apply framework-aligned calculations

### Step 2: Run Strategy-Specific Calculations

---

**BRRRR (Buy, Rehab, Rent, Refinance, Repeat):**

```
Purchase Price:              $X
Rehab Budget:                $X
Total Investment:            $X
After Repair Value (ARV):    $X
Refinance at 75% ARV:       $X
Cash Left in Deal:           $X  (Total Investment - Refi Amount)
Monthly Rent:                $X
Monthly Expenses:            $X  (PITI + vacancy + maint + mgmt)
Monthly Cash Flow:           $X
Annual Cash Flow:            $X
Cash-on-Cash Return:         X%  (Annual CF / Cash Left in Deal)
Infinite Return?             Yes/No (if cash left = $0 or less)
```

---

**Flip:**

```
Purchase Price:              $X
Rehab Budget:                $X
Holding Costs (X months):    $X  (mortgage, insurance, taxes, utilities)
Selling Costs (6%):          $X
Total Costs:                 $X
After Repair Value (ARV):    $X
Gross Profit:                $X  (ARV - Total Costs)
Net Profit:                  $X  (after taxes estimate)
ROI:                         X%
Annualized ROI:              X%  (if held < 12 months)
Profit per Month:            $X
```

---

**Buy and Hold:**

```
Purchase Price:              $X
Down Payment:                $X
Loan Amount:                 $X
Interest Rate:               X%
Monthly P&I:                 $X
Monthly Taxes:               $X
Monthly Insurance:           $X
Monthly Vacancy (8%):        $X
Monthly Maintenance (5%):    $X
Monthly Management (10%):    $X
Total Monthly Expenses:      $X
Monthly Rent:                $X
Monthly Cash Flow:           $X
Annual Cash Flow:            $X
Cap Rate:                    X%
Cash-on-Cash Return:         X%
GRM:                         X
DSCR:                        X
50% Rule Check:              $X vs $X (does it pass?)
1% Rule Check:               X% (does it pass?)

5-Year Projection:
| Year | Rent | Expenses | Cash Flow | Equity | Total Return |
|------|------|----------|-----------|--------|-------------|
```

---

**Seller Finance (Buying on Seller Terms):**

```
Purchase Price:              $X
Down Payment:                $X
Seller Note Amount:          $X
Interest Rate:               X%
Term:                        X years
Balloon (if any):            Year X, $X remaining
Monthly Payment:             $X
Monthly Rent:                $X
Monthly Cash Flow:           $X
Annual Cash Flow:            $X
Cash-on-Cash Return:         X%
Total Interest Paid:         $X
Balloon Payment Due:         $X on [date]
Exit Strategy at Balloon:    [Refinance / Sell / Renegotiate]
```

---

**SubTo (Subject To Existing Financing):**

```
Existing Mortgage Balance:   $X
Existing Payment (PITI):     $X
Existing Rate:               X%
Remaining Term:              X years
Cash to Seller:              $X
Total Money In:              $X
Monthly Rent:                $X
Monthly Cash Flow:           $X  (Rent - Existing PITI - Expenses)
Equity Position:             $X  (Market Value - Mortgage Balance)
Annual Cash Flow:            $X
Cash-on-Cash Return:         X%
Risk: Due-on-Sale:           [Assessment]
```

---

**Wrap (Selling on Terms / Note Creation):**

```
Acquisition Cost:            $X (purchase price or existing balance)
Your Payment:                $X/mo at X%
Sell Price:                  $X
Buyer Down Payment:          $X
Wrap Note Amount:            $X
Buyer Rate:                  X%
Buyer Term:                  X years
Buyer Payment:               $X/mo
Monthly Spread:              $X  (Buyer Payment - Your Payment)
Annual Spread:               $X
Front-End Profit:            $X  (Buyer Down - Cash to Seller)
Back-End Profit:             $X  (Principal paydown spread over term)
Total Profit (Lifetime):     $X
```

### Step 3: Sensitivity Analysis
Show how the deal changes with different assumptions:

| Variable | -10% | Base | +10% |
|----------|------|------|------|
| Rent | $X → X% CoC | $X → X% CoC | $X → X% CoC |
| Price | $X → X% CoC | $X → X% CoC | $X → X% CoC |
| Rate | X% → X% CoC | X% → X% CoC | X% → X% CoC |

### Step 4: Deal Verdict
- **Is this a good deal?** [Yes / No / Conditional]
- **Minimum rent needed to break even:** $X/mo
- **Maximum purchase price at target return:** $X
- **Best strategy for this deal:** [recommendation]

### Step 5: Save Calculations
- Save to `~/.claude/brain/deal-packages/[deal-slug]/investment-calc.md` if tied to a specific deal
- Otherwise display inline
- Offer to run additional scenarios with different numbers
