import React, { useState, useEffect } from "react";
import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
  Select,
} from "@mantine/core";
import { IconAt } from "@tabler/icons-react";
import { IconChevronDown } from "@tabler/icons-react";
import SignupHead from "../../components/SignupHead";

export default function TeacherRegister() {
  const [searchValue, onSearchChange] = useState("");
  const [classValue, onClassChange] = useState("");
  const [schoolTeacher, setSchoolTeacher] = useState(false);
  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <SignupHead title="Teacher" />

        <Paper withBorder shadow="md" p={30} mt={30} radius="md">
          <TextInput label="First Name" 
            my="md"
          required />
          <TextInput label="Last Name"
            my="md"
          required />
          <TextInput
            type="number"
            label="Phone Number"
            my="md"
            icon={<Text color="gray" ml="xr"> +237</Text>}
            required
          />
          <TextInput
            label="Email"
            placeholder="you@mantine.dev"
            icon={<IconAt size="0.8rem" />} 
            required />
            <Checkbox label="I am a school teacher" 
            onChange={() => setSchoolTeacher(!schoolTeacher)} 
            my="md"
            />
         {
            schoolTeacher && (
              <>
                <Select
                  mt="md"
                  label="Subsystem"
                  data={['English', 'French', 'Both']}
                  placeholder="Select Subsystem"
                  rightSection={<IconChevronDown size="1rem" />}
                  my="md"
                />
                <Select
                  mt="md"
                  label="Your School"
                  searchable
                  onSearchChange={onSearchChange}
                  searchValue={searchValue}
                  nothingFound="Your School is not listed"
                  my="md"
                  rightSection={<IconChevronDown size="1rem" />}
                  data={["React", "Angular", "Svelte", "Vue"]}
                />


              </>
            )
         }
          <PasswordInput
            label="Password"
            my="md"
            required
            mt="md"
          />
          <PasswordInput
            label="Confirm Password"
            my="md"
            required
            mt="md"
          />
          <Button
            fullWidth
            mt="xl"
            style={{
              backgroundColor: "#FFC107",
            }}
          >
            Sign in
          </Button>
        </Paper>
      </Container>
    </div>
  );
}
