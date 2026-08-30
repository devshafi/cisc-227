# Assignment 1: Requirements Elicitation via Role-Play

## Overview

In this assignment, you will practice **requirements elicitation**: eliciting
requirements for a system by role-playing its stakeholders, checking the
quality of those requirements against six standard attributes (conflict,
ambiguity, completeness, consistency, testability, evolvability), comparing
your work against an AI assistant's, and producing a final requirements list
you'll use again in Assignment 2.

To do this, you will choose one of three projects from the list: **Library
Management**, **Inventory Management**, or **Equipment Rental Management**.
Groups are two members, and the rules for choosing a project (shared
separately, to keep the process fair and avoid everyone piling onto the same
one) will be announced before this assignment starts.

Find your domain's materials in [assignment-1/library-management/](https://github.com/devshafi/cisc-227/tree/main/assignment-1/library-management/),
[assignment-1/inventory-management/](https://github.com/devshafi/cisc-227/tree/main/assignment-1/inventory-management/), or
[assignment-1/equipment-rental-management/](https://github.com/devshafi/cisc-227/tree/main/assignment-1/equipment-rental-management/):
- `scenario_brief.md`: the (intentionally incomplete) client brief
- `role_cards/`: one card per stakeholder role (there are 3 role cards per domain)
- Shared: [quality_check_worksheet.md](https://github.com/devshafi/cisc-227/blob/main/assignment-1/quality_check_worksheet.md), [prework_checklist.md](https://github.com/devshafi/cisc-227/blob/main/assignment-1/prework_checklist.md)

Once your group picks a domain, you stay on it for every assignment this term.

## Steps

1. **Pre-work** (individual, before the group session): complete
   [prework_checklist.md](https://github.com/devshafi/cisc-227/blob/main/assignment-1/prework_checklist.md) (editor, git, GitHub account, repo, TA invited).

2. **Read the scenario brief** for your chosen domain as a group. Do not read
   the other domain's materials or role cards; only its scenario brief is fair
   game if you're curious, but your requirements should come from your own
   domain's role-play.

3. **Role assignment**: there are 3 stakeholder role cards but only 2 of you,
   so each member picks one role card as their **primary role**. The third
   role card is **shared**, meaning both of you will read and role-play it
   together rather than assigning it to one person.

4. **Individual elicitation**:
   - For your primary role: your partner interviews you in-role (like a
     requirements analyst interviewing a stakeholder), then you swap and you
     interview them in their primary role. Each of you writes your **own**
     individual requirements list from your own primary role, in your own
     words. Use standard "the system shall..." style requirement statements.
   - For the shared third role: read the card together, discuss what that
     stakeholder would realistically want, and write **one joint list**
     for that role. If the two of you land on different interpretations of
     what that stakeholder wants, don't paper over it: that disagreement is
     worth capturing too.
   - You should end this step with 3 requirements lists total: 2 individual
     (one per member) + 1 joint.

5. **Group consolidation**: as a group, merge the individual lists into one
   consolidated requirements list. Run every requirement through the
   quality-check worksheet (conflict, ambiguity, completeness, consistency,
   testability, evolvability). Pay particular attention to any point where two
   stakeholders' role cards pulled in different directions: that's a real
   conflict, not a mistake, and it should be documented, not silently dropped.

6. **AI comparison**: give an AI assistant (e.g. Claude, ChatGPT) only the
   `scenario_brief.md` (not your role cards or your own list) and ask it to
   generate a requirements list for the system. Run the same quality-check
   worksheet on the AI's list.

7. **Comparison write-up** (0.5-1 page): what did the AI's list miss that your
   role-play surfaced (especially the planted stakeholder conflict)? What did
   the AI invent or assume that wasn't grounded in any stakeholder's actual
   need? Where did the two lists agree?

8. **Final requirements list**: produce your group's final, refined
   requirements list, incorporating anything useful from the AI pass. Keep
   this list, since you will compare it against the actual running
   application's behavior in Assignment 2.

## Deliverables (submit to OnQ as one PDF, code/checklist confirmation via GitHub)

1. Role-based requirements lists: 2 individual (one per member, labeled by role) + 1 joint (for the shared third role)
2. Group consolidated requirements list + completed quality-check worksheet
3. AI-generated requirements list + completed quality-check worksheet
4. Comparison write-up (own vs. AI)
5. Final requirements list
6. Pre-work checklist confirmation (repo link, TA invited)

## Grading Scheme

| Component | Marks |
|---|---|
| Role-based requirements lists (2 individual + 1 joint) | 1.5 |
| Group consolidated list + quality-check worksheet | 3 |
| AI-generated list + quality-check worksheet | 1.5 |
| Comparison write-up | 2 |
| Final requirements list quality | 1.5 |
| Pre-work checklist completion | 0.5 |
| **Total** | **10** |
