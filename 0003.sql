
--
-- Change Meta options on borrow
--
--
-- Change Meta options on reserve
--
--
-- Rename field isourdated on reserve to isbookavaiable
--
ALTER TABLE "LIBRARY_RESERVE" RENAME COLUMN "ISOURDATED" TO "ISBOOKAVAIABLE";
ALTER TABLE "LIBRARY_RESERVE" ADD CONSTRAINT "LIBRARY_R_ISBOOKAVA_C5AF2136_C" CHECK ("ISBOOKAVAIABLE" IN (0,1));
--
-- Add field adddate to reserve
--
ALTER TABLE "LIBRARY_RESERVE" ADD "ADDDATE" DATE DEFAULT '2019-12-21' NOT NULL;
ALTER TABLE "LIBRARY_RESERVE" MODIFY "ADDDATE" DEFAULT NULL;
COMMIT;
